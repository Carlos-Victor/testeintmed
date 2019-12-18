<template>
  <div id="app">
    <v-app id="inspire">
      <v-app-bar app color="indigo" dark>
        <v-toolbar-title>Application</v-toolbar-title>
      </v-app-bar>

      <v-content>
        <v-container fluid fill-height>
          <v-layout align-center justify-center>
            <v-flex text-xs-center>
              <v-form ref="form" v-model="valid" lazy-validation>
                {{ processador }}
                {{ placa_mae }}
                {{ memoria }}
                {{ tamanho_da_memoria }}
                {{ placa_de_video }}
                <v-select
                  v-model="placa_mae"
                  :items="placa_mae_item"
                  item-text="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Placa Mãe"
                  required
                ></v-select>
                <v-select
                  v-model="processador"
                  :items="processador_item"
                  item-text="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Processador"
                  required
                ></v-select>
                <v-select
                  v-model="memoria"
                  :items="memoria_item"
                  item-text="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Memoria"
                  required
                ></v-select>
                <v-select
                  v-model="tamanho_da_memoria"
                  :items="tamanho_de_memoria_item"
                  item-text="produto"
                  :rules="[v => !!v || 'Você precisa selecionar um item']"
                  label="Tamanho da Memoria"
                  required
                ></v-select>
                <v-text-field
                  v-model="qnt_memoria"
                  :counter="2"
                  type="number"
                  :rules="numberRules"
                  label="Quantidade de mémoria"
                  required
                ></v-text-field>
                <v-select
                  v-model="placa_de_video"
                  :items="placa_de_video_item"
                  item-text="produto"
                  label="Placa de vídeo"
                ></v-select>

                <v-btn
                  :disabled="!valid"
                  color="success"
                  class="mr-4"
                  @click="validate"
                >
                  Enviar
                </v-btn>

                <v-btn color="error" class="mr-4" @click="reset">
                  Reset Form
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
export default {
  data: () => ({
    valid: true,
    processador_item: "",
    placa_mae_item: "",
    memoria_item: "",
    placa_de_video_item: "",
    qntnumber: "",
    numberRules: [v => !!v || "Você precisa digitar a quantidade de memoria"],
    select: null,
    tamanho_de_memoria_item: ["4GB", "8GB", "16GB", "32GB", "64GB"]
  }),
  mounted() {
    const axios = require("axios");
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
    
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
      }
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>
