<template>
  <v-main class="vmain" pa-0>
    <v-card max-width="600" class="mx-auto my-5">
      <v-text-field
        v-model="keyword"
        prepend-inner-icon="mdi-magnify"
        label="検索"
        single-line
        hide-details
        @keydown.enter="search(keyword, 2)"
      ></v-text-field>
      <v-btn color="primary" width="50%" @click="search(keyword, 1)"
        >完全一致検索</v-btn
      ><v-btn color="primary" width="50%" @click="search(keyword, 2)"
        >gooAPI検索</v-btn
      >
    </v-card>
    <v-card v-if="beforeSearch">
      <v-card-text>
        <p>検索してください</p>
      </v-card-text>
    </v-card>
    <v-card v-else>
      <v-card-title v-if="loading"
        >検索中.....<v-progress-circular
          indeterminate
          color="primary"
        ></v-progress-circular
      ></v-card-title>
      <v-card-title v-else
        >検索結果 {{ state.count }}件 - {{ state.keyword }}</v-card-title
      >
      <v-container>
        <v-row>
          <v-col v-for="item in state.items" :key="item.id">
            <v-card ma-2 width="320">
              <v-list-item-title>Room{{ item.room_id }}-Cam {{ item.camera_id }}-User:{{ item.user }}</v-list-item-title>
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
    <v-container>
      <v-spacer></v-spacer>
      <v-card class="goocredit">
        <v-card-text>
          GooAPI検索は、<a href="https://labs.goo.ne.jp/api/textpair_doc"
            >テキストペア類似度API</a
          >を使用しています。
        </v-card-text>
        <a href="http://www.goo.ne.jp/">
          <v-img
            src="//u.xgoo.jp/img/sgoo.png"
            alt="supported by goo"
            title="supported by goo"
          />
        </a>
      </v-card>
      <v-spacer></v-spacer>
    </v-container>
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
.vmain {
  background-color: lightsteelblue;
  height: 100%;
  justify-content: center;
}
.center {
  display: flex;
  justify-content: center; /* 横方向に中央揃え */
  align-items: center; /* 縦方向に中央揃え */
}
/*横幅が300px以下の場合に適用*/
@media screen and (max-width: 300px) {
  .goocredit {
    width: 100%;
  }
}
@media screen and (min-width: 300px) {
  .goocredit {
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    width: 300px;
  }
}
</style>
