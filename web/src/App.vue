<template>
  <div id="app">
    <Header class="header" />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export default {
  name: "App",
  components: { Header, Footer }
};
</script>

<style>
#app {
  font-family: "Pangram", sans-serif !important;
  margin-top: 0;
  text-align: center;
}
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 50px;
  display: inline-block;
}
</style>
