<template>
  <div id="app">
    <v-app id="inspire">
      <v-app-bar app color="indigo" dark>
        <v-toolbar-title>Silvertec Informática</v-toolbar-title>
      </v-app-bar>

      <v-content>
        <v-container fluid fill-height>
          <v-layout align-center justify-center>
            <v-flex text-xs-center>
              <v-form ref="form" v-model="valid" lazy-validation>
                <v-autocomplete
                  v-model="montar.placa_mae"
                  :items="placa_mae_item"
                  item-value="produto"
                  item-text="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Placa Mãe"
                  no-data-text="Nenhuma placa mãe encontrada"
                  required
                ></v-autocomplete>
                <v-autocomplete
                  v-model="montar.processador"
                  :items="processador_item"
                  item-value="produto"
                  item-text="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Processador"
                  no-data-text="Nenhum processador encontrada"
                  required
                ></v-autocomplete>
                <v-autocomplete
                  v-model="montar.memoria"
                  :items="memoria_item"
                  item-text="produto"
                  item-value="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Memoria"
                  no-data-text="Nenhuma memoria encontrada"
                  required
                ></v-autocomplete>
                <v-autocomplete
                  v-model="montar.tamanho_da_memoria"
                  :items="tamanho_de_memoria_item"
                  item-text="produto"
                  item-value="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Tamanho da Memoria"
                  required
                ></v-autocomplete>
                <v-text-field
                  v-model="montar.quantidade_de_memoria"
                  :counter="2"
                  type="number"
                  :rules="numberRules"
                  label="Quantidade de mémoria"
                  required
                ></v-text-field>
                <v-autocomplete
                  v-model="montar.placa_de_video"
                  :items="placa_de_video_item"
                  item-value="produto"
                  item-text="produto"
                  label="Placa de vídeo"
                  no-data-text="Nenhuma placa de video encontrada"
                ></v-autocomplete>

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
        <span class="white--text">&copy; 2019 - Carlos Victor</span>
      </v-footer>
    </v-app>
  </div>
</template>

<script>
import axios from "axios";
import swal from "sweetalert";

export default {
  data: () => ({
    valid: true,
    processador_item : null,
    placa_de_video_item :null,
    placa_mae_item: null,
    memoria_item: null,
    montar: {
      processador: null,
      placa_mae: null,
      memoria: null,
      placa_de_video: null,
      quantidade_de_memoria: null
    },
    numberRules: [v => !!v || "Você precisa digitar a quantidade de memoria"],
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
      axios
        .post("http://127.0.0.1:8081/api/monteseupc/", montar, {
          headers: {
            Authorization: "Token 2c04b7e063a330162cfca2e7a434db96e58671b7"
          }
        })
        .then(response => {
          if (response.status == 201) {
            swal({
              title: "Pedido Realizado com Sucesso",
              icon: "success",
              button: "OK"
            });
          }
        })
        .catch(function(error) {
          if (error.response.status != 201) {
            swal({
              title: "Erro ao realizar pedido",
              text: error.response.data.non_field_errors[0],
              icon: "error",
              button: "OK"
            });
          }
        });
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>


<style>
.swal-text{
  font-weight:600;
  text-align: center;
  text-transform: capitalize;
}

</style>