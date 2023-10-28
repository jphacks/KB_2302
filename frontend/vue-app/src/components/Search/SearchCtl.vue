<template>
  <v-main>
    <v-card max-width="600" class="mx-auto">
      <v-text-field
        v-model="state.keyword"
        append-icon="mdi-magnify"
        label="検索"
        single-line
        hide-details
        @keydown.enter="search(state.keyword)"
      ></v-text-field>
      <v-btn color="primary" width="100%" @click="search(state.keyword)"
        >検索</v-btn
      >
    </v-card>
    <v-card v-if="beforeSearch">
      <v-card-text>
        <p>検索してください</p>
      </v-card-text>
    </v-card>
    <v-card v-else>
      <v-card-title
        >検索結果 {{ state.count }}件 - {{ state.keyword }}</v-card-title
      >
      <v-container>
        <v-row>
          <v-col v-for="item in state.items" :key="item.id" cols="3">
            <v-card ma-2>
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
  </v-main>
</template>
  
  <script>
import { reactive, ref } from "vue";
import axios from "axios";
export default {
  setup() {
    const beforeSearch = ref(true);
    const state = reactive({
      keyword: null,
      items: [],
    });
    function openImageInNewTab(url) {
      window.open(url, "_blank");
    }
    function search(keyword) {
      this.beforeSearch = false;
      axios
        .get(`https://kb2302-develop.onrender.com/search/label/v1?q=${keyword}`)
        .then((response) => {
          this.state.count = response.data.count;
          this.state.items = response.data.contents;
          return true;
        })
        .catch((error) => {
          console.log(error);
          return false;
        });
    }
    return {
      state,
      search,
      openImageInNewTab,
      beforeSearch,
    };
  },
};
</script>
    
