<template>
  <v-main>
    <v-card class="desccard">
      <v-card-title>背景（製品開発のきっかけ、課題等）</v-card-title>
      <v-card-text>
        私たちは衛星開発を複数人で行うにあたって，道具や部品が散らばったり，無くなったりする事がよくある．それは自分がどこにしまったか忘れてしまっていることや，他の人が移動させたことが原因で起きており，この問題は研究室や作業部屋といった複数人で空間を共有するケースや個人の家の中であっても起こりうるものである． こういった課題を解決するAirTagといった製品は需要があり，徐々に浸透してきているが，タグはそれ自体が高価であったり，取り付けにくいものがあるなどから，紛失防止が十分に達成されているとは言えないと思われる． 私たちはこういった問題を解決するべく，より多くのものの捜索を行うことができるサービスを実現したいと考え，AIの画像認識を用いた物体追跡により，もの探しを支援するアプリの開発に至った．
      </v-card-text>
    </v-card>
    <v-card class="desccard">
      <v-card-title>カメラでのトラッキングと紛失検知の動画</v-card-title>
      <iframe
        width="560"
        height="315"
        src="https://www.youtube.com/embed/tChvnhBinck?si=QWvnVPIeAxQZCMmr"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
      ></iframe>
    </v-card>
    <v-card class="desccard">
      <v-card-title>紛失検知と検索のデモ動画</v-card-title>
      <iframe
        width="560"
        height="315"
        src="https://www.youtube-nocookie.com/embed/4I6-guNvUiY?si=tWYtrxu8WT7nxr-s"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
      ></iframe>
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
    margin-top: 20px;
    left: 50%;
    transform: translateX(-50%);
    max-width: 600px;
    background-color: lightsteelblue;
  }
}
</style>