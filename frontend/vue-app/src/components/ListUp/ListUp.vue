<template>
    <v-main class="vmain" pa-0>
      <v-card v-if="beforeSearch" my-5>
        <v-btn color="primary" class="loadbtn" @click="search()">撮影済みラベル一覧を取得</v-btn>
      </v-card>
      <v-card v-else>
        <v-card-title v-if="loading"
          >取得中.....<v-progress-circular
            indeterminate
            color="primary"
          ></v-progress-circular
        ></v-card-title>
        <v-card-title v-else
          >取得結果 {{ state.count }}件 - 撮影済みラベル一覧</v-card-title
        >
        <v-container>
          <v-row>
            <v-col v-for="item in state.items" :key="item.id">
              <v-card ma-2 width="320">
                <v-list-item-title>Label: {{ item.label }}</v-list-item-title>
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
    name: "ListUp",
    setup() {
      const beforeSearch = ref(true);
      const loading = ref(false);
      const state = reactive({
        count: 0,
        items: [],
      });
      const keyword = ref("");
      function openImageInNewTab(url) {
        window.open(url, "_blank");
      }
      function search() {
        this.loading = true;
        this.beforeSearch = false;
        const url = `https://kb2302-develop.onrender.com/getlist/v1`;
        axios
          .get(url)
          .then((response) => {
            console.log(response.data.contents);
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
  .loadbtn{
    position: relative;
    margin-top: 50px;
    left: 50%;
    transform: translateX(-50%);
  }
  </style>
  