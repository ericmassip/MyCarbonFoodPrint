<template>
  <div>
    <b-card class="bg-light text-center" style="border:0">
      <div>
        Built with <span style="color:red">&hearts;</span> by the Dream Team
      </div>
      <div style="padding-top:10px">
        <a href="https://github.com/victorjgf">Victor</a>
        &emsp;&emsp;&emsp;&emsp;
        <a href="https://github.com/RushilDaya">Rushil</a>
        &emsp;&emsp;&emsp;&emsp;
        <a href="https://github.com/IgnacioGarrido">Nacho</a>
        &emsp;&emsp;&emsp;&emsp;
        <a href="https://github.com/murilo-cunha">Murilo</a>
        &emsp;&emsp;&emsp;&emsp;
        <a href="https://github.com/ericmassip">Erick</a>
      </div>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "FooterArea",
  data() {
    return {};
  },
  methods: {
    goMainScreen() {
      this.$router.push("/");
    },
    goMapScreen() {
      this.$router.push("/map");
    }
  }
};
</script>

<style scoped></style>
