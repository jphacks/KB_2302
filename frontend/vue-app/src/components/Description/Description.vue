<template>
  <v-main>
    <v-card class="desccard">
      <v-card-title>このサービスについて アイデア</v-card-title>
      <v-card-text>
        日々の生活の中で、物が紛失することが多くあります。近年、AirtagやTileなどの紛失防止タグが登場していることから、もの探しの効率化が望まれていることが伺われます。しかしながら、これらのタグは高価でかさばるため、日用品全てに使用することは難しい状況です。この課題に対して、カメラを用いたもの探し支援アプリを開発いたしました。カメラで撮影したデータをAIによって処理することで、物体を追跡し、物がしまわれた、持ち出されたなどの情報を検知・記録することができます。使用者は、検索フォームから無くしたものを探すことができます。
      </v-card-text>
    </v-card>
  </v-main>
</template>
<script>
export default {
  name: "PageDescription",
};
</script>
<style scoped>
@media screen and (max-width: 300px) {
  .desccard {
    width: 100%;
  }
}
@media screen and (min-width: 300px) {
  .desccard {
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    width: 600px;
  }
}
</style>