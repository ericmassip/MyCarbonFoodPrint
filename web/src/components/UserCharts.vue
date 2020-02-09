<template>
  <b-container class="user-charts" id="user-charts">
    <b-row>
      <b-col>
        <Plotly
          v-show="isFoodItemsChartActive"
          :data="co2ProductionFoodData"
          :layout="co2ProductionFoodDataLayout"
          :display-mode-bar="false"
        />
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <Plotly
          v-show="isFoodItemsChartActive"
          :data="co2ProductionFoodGroupData"
          :layout="co2ProductionFoodGroupDataLayout"
          :display-mode-bar="false"
        />
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <Plotly
          v-show="this.user.country != null && this.user.agegroup != null"
          :data="co2AvgWeeklyComparison"
          :layout="co2AvgWeeklyComparisonLayout"
          :display-mode-bar="false"
        />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { Plotly } from "vue-plotly";

export default {
  name: "UserCharts",
  components: {
    Plotly
  },
  props: [
    "user",
    "isFoodItemsChartActive",
    "co2ProductionFoodData",
    "co2ProductionFoodGroupData",
    "co2AvgWeeklyComparison"
  ],
  data() {
    return {
      co2ProductionFoodDataLayout: {
        title: "My CO2 Production per Food Item",
        yaxis: {
          title: {
            text: "CO2 Footprint (grams)"
          }
        }
      },
      co2ProductionFoodGroupDataLayout: {
        title: "My CO2 Production per Food Group",
        yaxis: {
          title: {
            text: "CO2 Footprint (grams)"
          }
        }
      },
      co2AvgWeeklyComparisonLayout: {
        title: "Country Comparison",
        yaxis: {
          title: {
            text: "CO2 Footprint (grams)"
          }
        }
      }
    };
  }
};
</script>

<style>
.user-charts {
  padding: 10px;
}
</style>
