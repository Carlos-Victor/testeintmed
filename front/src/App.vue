<template>
  <div id="app">
    <v-app id="inspire">
      <v-app-bar app color="indigo" dark>
        <v-toolbar-title>Monte seu PC</v-toolbar-title>
      </v-app-bar>

      <v-content>
        <v-container fluid fill-height>
          <v-layout align-center justify-center>
            <v-flex text-xs-center>
              <v-form ref="form" v-model="valid" lazy-validation>
                {{ montar.processador }}
                {{ montar.placa_mae }}
                {{ montar.memoria }}
                {{ montar.tamanho_da_memoria }}
                {{ montar.placa_de_video }}
                {{ montar.qnt_memoria }}
                <v-select
                  v-model="montar.placa_mae"
                  :items="placa_mae_item"
                  item-value="produto"
                  item-text="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Placa Mãe"
                  no-data-text="Nenhuma placa mãe encontrada"
                  required
                ></v-select>
                <v-select
                  v-model="montar.processador"
                  :items="processador_item"
                  item-value="produto"
                  item-text="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Processador"
                  no-data-text="Nenhum processador encontrada"
                  required
                ></v-select>
                <v-select
                  v-model="montar.memoria"
                  :items="memoria_item"
                  item-text="produto"
                  item-value="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Memoria"
                  no-data-text="Nenhuma memoria encontrada"
                  required
                ></v-select>
                <v-select
                  v-model="montar.tamanho_da_memoria"
                  :items="tamanho_de_memoria_item"
                  item-text="produto"
                  item-value="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Tamanho da Memoria"
                  required
                ></v-select>
                <v-text-field
                  v-model="montar.quantidade_de_memoria"
                  :counter="2"
                  type="number"
                  :rules="numberRules"
                  label="Quantidade de mémoria"
                  required
                ></v-text-field>
                <v-select
                  v-model="montar.placa_de_video"
                  :items="placa_de_video_item"
                  item-value="produto"
                  item-text="produto"
                  label="Placa de vídeo"
                  no-data-text="Nenhuma placa de video encontrada"
                ></v-select>

                <v-btn
                  :disabled="!valid"
                  color="success"
                  class="mr-4"
                  @click="salvar_montagem(montar)"
                >
                  Enviar
                </v-btn>

                <v-btn color="error" class="mr-4" @click="reset">
                  Limpar Formulario
                </v-btn>
              </v-form>
            </v-flex>
          </v-layout>
        </v-container>
      </v-content>
      <v-footer color="indigo" app>
        <span class="white--text">&copy; 2019</span>
      </v-footer>
    </v-app>
  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert';

export default {
  data: () => ({
    valid: true,
    montar:{
    processador_item: null,
    placa_mae_item: null,
    memoria_item: null,
    placa_de_video_item: null,
    quantidade_de_memoria: null
    },
    numberRules: [v => !!v || "Você precisa digitar a quantidade de memoria"],
    select: null,
    tamanho_de_memoria_item: ["4GB", "8GB", "16GB", "32GB", "64GB"]
  }),
  mounted() {
    axios
      .get("http://127.0.0.1:8081/api/processadores/", {
        headers: {
          Authorization: "Token 2c04b7e063a330162cfca2e7a434db96e58671b7"
        }
      })
      .then(response => (this.processador_item = response.data)),
      axios
        .get("http://127.0.0.1:8081/api/placamaes/", {
          headers: {
            Authorization: "Token 2c04b7e063a330162cfca2e7a434db96e58671b7"
          }
        })
        .then(response => (this.placa_mae_item = response.data)),
      axios
        .get("http://127.0.0.1:8081/api/memorias/", {
          headers: {
            Authorization: "Token 2c04b7e063a330162cfca2e7a434db96e58671b7"
          }
        })
        .then(response => (this.memoria_item = response.data)),
      axios
        .get("http://127.0.0.1:8081/api/placasdevideo/", {
          headers: {
            Authorization: "Token 2c04b7e063a330162cfca2e7a434db96e58671b7"
          }
        })
        .then(response => (this.placa_de_video_item = response.data));
  },
    methods: {
    salvar_montagem(montar) {
        axios.post("http://127.0.0.1:8081/api/monteseupc/", montar,{
          headers: {
          Authorization: "Token 2c04b7e063a330162cfca2e7a434db96e58671b7"
        }
        }).then(response => {
          if (response.status == 201){
              swal({
                title: "Pedido Realizado",
                text: "Pedido Realizado com Sucesso",
                icon: "success",
                button: "OK",
              })}
            }).catch(function (error) {
        if (error.response.status != 201){
          swal({
                title: "Erro ao realizar pedido",
                text: error.response.data.non_field_errors[0],
                icon: "error",
                button: "OK",
              })
        }
    })
    },
    reset() {
      this.$refs.form.reset();
    }
    },
};
</script>
