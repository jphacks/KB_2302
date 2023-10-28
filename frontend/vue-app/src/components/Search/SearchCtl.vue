<template>
  <v-main>
    <v-card v-if="beforeSearch" max-width="600" class="mx-auto">
      <v-text-field
        v-model="keyword"
        append-icon="mdi-magnify"
        label="検索"
        single-line
        hide-details
      ></v-text-field>
      <v-btn color="primary" @click="search(keyword)">検索</v-btn>
    </v-card>
  </v-main>
</template>
  
  <script>
import { reactive } from "vue";
import axios from "axios";
export default {
  setup() {
    const state = reactive({
      keyword: null,
      items: [],
    });
    let beforeSearch = true;

    function search(keyword) {
      beforeSearch = false;
      axios
        .get(`https://example.com/api/search?q=${keyword}`)
        .then((response) => {
          state.items = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    }

    return {
      keyword: state.keyword,
      items: state.items,
      search,
      beforeSearch,
    };
  },
};
</script>
    
