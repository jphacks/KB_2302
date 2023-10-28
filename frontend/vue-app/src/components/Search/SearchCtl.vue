<template>
  <v-main>
    <v-card max-width="600" class="mx-auto">
      <v-text-field
        v-model="state.keyword"
        append-icon="mdi-magnify"
        label="検索"
        single-line
        hide-details
      ></v-text-field>
      <v-btn color="primary" @click="search(state.keyword)">検索</v-btn>
    </v-card>
    <v-card v-if="beforeSearch">
      <v-card-text>
        <p>検索してください</p>
      </v-card-text>
    </v-card>
    <v-card v-else>
      <v-card-title>検索結果 {{ state.count }}件</v-card-title>
      <v-card-text>
        <v-list>
          <v-list-item v-for="item in state.items" :key="item.id">
              <v-list-item-title>{{ item.label }}</v-list-item-title>
              <img v-bind:src="item.imgURL" width="300" />
              <p>{{ item.time }} / {{ item.room_id }}</p>
          </v-list-item>
        </v-list>
      </v-card-text>
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

    function search(keyword) {
      this.beforeSearch = false;
      axios
        .get(`https://kb2302-develop.onrender.com/search/label/v1?q=${keyword}`)
        .then((response) => {
          console.log(response.data.contents);
          this.state.count = response.data.count;
          this.state.items = response.data.contents;
        })
        .catch((error) => {
          console.log(error);
        });
    }
    return {
      state,
      search,
      beforeSearch,
    };
  },
};
</script>
    
