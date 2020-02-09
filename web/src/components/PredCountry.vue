<template>
  <div id="country-pred">
    <p>
      Based on your weekly food intake, you are probably from:
      <!--{{country_pred}}-->
    </p>
  </div>
</template>

<script>
export default {
  name:
    "CountryPred" /*,
  data(){
    return{
      country_pred:''
    }
  },
  mounted(){
    this.$http.get(this.FLASK_URL+'/api/predict_country')
    .then(response => {
      this.country_pred = response.data
    })
  }*/
};
</script>

<style scoped></style>
