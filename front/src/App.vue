<template>
  <v-app>
    <v-content>
      <Montar />
    </v-content>
  </v-app>
</template>

<script>
import Montar from './components/montarpc.vue'


export default {
  name: 'App',
  components: {
    Montar,
    // Login,
  },


  data: () => ({
    //
  }),
};
</script>