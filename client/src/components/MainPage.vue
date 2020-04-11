<template>
  <b-container id="main-page">
    <UserInputForm :user="user" />
    <UserFootprintGauge
      :userCarbonFootprint="userCarbonFootprint"
      :countryCarbonFootprint="countryCarbonFootprint"
    />
    <UserCharts
      :user="user"
      :isFoodItemsChartActive="isFoodItemsChartActive"
      :co2ProductionFoodData="co2ProductionFoodData"
      :co2ProductionFoodGroupData="co2ProductionFoodGroupData"
      :co2AvgWeeklyComparison="co2AvgWeeklyComparison"
    />
  </b-container>
</template>

<script>
import axios from 'axios';
import UserInputForm from '@/components/UserInputForm';
import UserFootprintGauge from '@/components/UserFootprintGauge';
import UserCharts from '@/components/UserCharts';

export default {
  name: 'MainPage',
  components: {
    UserInputForm,
    UserFootprintGauge,
    UserCharts
  },
  data() {
    return {
      user: {
        country: null,
        agegroup: null,
        foodItems: {
          fruit: [],
          grain: [],
          vegetable: [],
          dairy: [],
          nut_seed_legume: [],
          meat: [],
          oil: [],
          other: []
        }
      },
      countriesCarbonFootprint: [],
      countryCarbonFootprint: 0,
      userCarbonFootprint: 0,
      co2ProductionFoodData: this.getEmptyBarChart(),
      co2ProductionFoodGroupData: this.getEmptyBarChart(),
      co2AvgWeeklyComparison: this.getEmptyBarChart(),
      isFoodItemsChartActive: false
    };
  },
  watch: {
    user: {
      handler: function() {
        this.computeCountryCarbonFootprint();
        this.computeUserCarbonFootprint();
        this.computeCountriesCarbonFootprint();
      },
      deep: true
    }
  },
  methods: {
    computeCountryCarbonFootprint() {
      try {
        if (this.user.country != null && this.user.agegroup != null) {
          axios
            .get(
              '/food/carbonfootprint/' +
                this.user.country +
                '/' +
                this.user.agegroup
            )
            .then(response => {
              this.countryCarbonFootprint = parseFloat(response.data);
            });
        }
      } catch (err) {
        this.countryCarbonFootprint = 0;
      }
    },
    computeUserCarbonFootprint() {
      this.co2ProductionFoodData = this.getEmptyBarChart();
      this.co2ProductionFoodGroupData = this.getEmptyBarChart();
      this.isFoodItemsChartActive = false;

      for (let category in this.user.foodItems) {
        if (this.user.foodItems[category][length] != 0) {
          var categoryCo2 = 0;

          for (const foodItem of this.user.foodItems[category]) {
            var foodItemCo2 =
              foodItem.grams_co2_per_serving * foodItem.quantity;

            this.userCarbonFootprint += foodItemCo2;
            categoryCo2 += foodItemCo2;

            this.co2ProductionFoodData[0].x.push(foodItem.name);
            this.co2ProductionFoodData[0].y.push(foodItemCo2);

            if (foodItem.quantity > 0) {
              this.isFoodItemsChartActive = true;
            }
          }

          this.co2ProductionFoodGroupData[0].x.push(
            category.charAt(0).toUpperCase() + category.slice(1)
          );
          this.co2ProductionFoodGroupData[0].y.push(categoryCo2);
        }
      }
      this.userCarbonFootprint = parseFloat(
        (this.userCarbonFootprint / 1000).toFixed(1)
      );
    },
    computeCountriesCarbonFootprint() {
      if (this.user.agegroup != null) {
        axios
          .get(
            '/country/carbonfootprint/all/' +
              this.user.agegroup +
              '/' +
              this.userCarbonFootprint
          )
          .then(response => {
            this.countriesCarbonFootprint = response.data;
            this.computeCo2AvgWeeklyComparison();
          });
      }
    },
    computeCo2AvgWeeklyComparison() {
      this.co2AvgWeeklyComparison = this.getEmptyBarChart();

      for (const country of this.countriesCarbonFootprint) {
        this.co2AvgWeeklyComparison[0].x.push(country.name);
        this.co2AvgWeeklyComparison[0].y.push(country.carbonFootprint);
      }

      this.co2AvgWeeklyComparison[0].marker.color = this.co2AvgWeeklyComparison[0].x.map(
        function(v) {
          return v == 'YOU' ? '#28a745' : '#007bff';
        }
      );
    },
    getEmptyBarChart() {
      return [
        {
          x: [],
          y: [],
          marker: {
            color: '#007bff'
          },
          type: 'bar'
        }
      ];
    }
  }
};
</script>

<style></style>
