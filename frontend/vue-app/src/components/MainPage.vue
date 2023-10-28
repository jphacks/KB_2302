<template>
  <v-main>
    <v-card>
      <v-card-title>JPHACKS KB_2302 なくしものさがし</v-card-title>
    </v-card>
    <v-tabs v-model="tab" bg-color="primary">
      <v-tab value="one">検索</v-tab>
      <v-tab value="two">捜索物一覧</v-tab>
      <v-tab value="three">説明</v-tab>
    </v-tabs>

    <v-window v-model="tab">
      <v-window-item value="one">
        <SearchCtl />
      </v-window-item>
    
      <v-window-item value="two"> Two </v-window-item>

      <v-window-item value="three"> Three </v-window-item>
    </v-window>
  </v-main>
</template>
<script>

import SearchCtl from "./Search/SearchCtl.vue";

export default {
  name: "MainPage",
  components: {
    SearchCtl,
  },
  data: () => ({
    tab: null,
  }),
};
</script>
