<template>
  <v-main>
    <v-card max-width="600" class="mx-auto">
      <v-text-field
        v-model="keyword"
        append-icon="mdi-magnify"
        label="検索"
        single-line
        hide-details
        @keydown.enter="search(keyword, 1)"
      ></v-text-field>
      <v-btn color="primary" width="50%" @click="search(keyword, 1)"
        >検索1</v-btn
      ><v-btn color="primary" width="50%" @click="search(keyword, 2)"
        >検索2</v-btn
      >
    </v-card>
    <v-card v-if="beforeSearch">
      <v-card-text>
        <p>検索してください</p>
      </v-card-text>
    </v-card>
    <v-card v-else>
      <v-card-title v-if="loading">検索中.....</v-card-title>
      <v-card-title v-else
        >検索結果 {{ state.count }}件 - {{ state.keyword }}</v-card-title
      >
      <v-container>
        <v-row>
          <v-col v-for="item in state.items" :key="item.id">
            <v-card ma-2 width="320">
              <v-list-item-title>Room{{ item.room_id }}</v-list-item-title>
              <img v-bind:src="item.imgURL" width="300" />
              <p>{{ item.time }}</p>
              <!--新しいタブで画像を開くボタン-->
              <v-btn
                color="primary"
                text
                @click="openImageInNewTab(item.imgURL)"
                >画像を見る</v-btn
              >
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
    <a href="http://www.goo.ne.jp/"  class="center">
      <img
        src="//u.xgoo.jp/img/sgoo.png"
        max-width="50"
        alt="supported by goo"
        title="supported by goo"
      />
    </a>
  </v-main>
</template>
  
  <script>
import { reactive, ref } from "vue";
import axios from "axios";
export default {
  setup() {
    const beforeSearch = ref(true);
    const loading = ref(false);
    const state = reactive({
      keyword: null,
      items: [],
    });
    const keyword = ref("");
    function openImageInNewTab(url) {
      window.open(url, "_blank");
    }
    function search(keyword, type) {
      this.loading = true;
      this.state.keyword = keyword;
      this.beforeSearch = false;
      let url = "";
      if (type == 2) {
        url = `https://kb2302-develop.onrender.com/search/word/v1?q=${keyword}`;
      } else {
        url = `https://kb2302-develop.onrender.com/search/label/v1?q=${keyword}`;
      }
      axios
        .get(url)
        .then((response) => {
          this.state.count = response.data.count;
          this.state.items = response.data.contents;
          this.loading = false;
          return true;
        })
        .catch((error) => {
          console.log(error);
          this.loading = false;
          return false;
        });
    }
    return {
      loading,
      keyword,
      state,
      search,
      openImageInNewTab,
      beforeSearch,
    };
  },
};
</script>
    <style scoped>
    .center {
  display: flex;
  justify-content: center; /* 横方向に中央揃え */
  align-items: center; /* 縦方向に中央揃え */
}
</style>
