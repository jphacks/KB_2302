<template>
  <v-main>
    <v-card>
      <v-card-title>JPHACKS KB_2302 探しAI(さがしあい)</v-card-title>
      <v-card-subtitle>～探し物 × Tech～</v-card-subtitle>
    </v-card>
    <v-tabs v-model="tab" bg-color="primary">
      <v-tab value="one">検索</v-tab>
      <v-tab value="two">捜索物一覧</v-tab>
      <v-tab value="three">説明</v-tab>
    </v-tabs>

    <v-window v-model="tab" bg-color="primary">
      <v-window-item value="one">
        <SearchCtl />
      </v-window-item>
      <v-window-item value="two">
        <ListUp />
      </v-window-item>
      <v-window-item value="three">
        <Description />
      </v-window-item>
    </v-window>
  </v-main>
</template>
<script>
import SearchCtl from "./Search/SearchCtl.vue";
import ListUp from "./ListUp/ListUp.vue";
import Description from "./Description/Description.vue";

export default {
  name: "MainPage",
  components: {
    SearchCtl,
    ListUp,
    Description,
  },
  data: () => ({
    tab: null,
  }),
};
</script>
