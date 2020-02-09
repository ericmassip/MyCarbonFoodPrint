<template>
  <b-container id="user-input-form">
    <b-row>
      <b-col>
        <h5 style="padding-top:10px;padding-bottom:10px;text-align:left;">
          <strong>Welcome to My Carbon Food Print!</strong>
        </h5>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <h6 style="padding-bottom:10px;text-align:left;">
          Fill in your country and age group to start calculating your
          <strong>Carbon Food Print</strong>!
        </h6>
      </b-col>
    </b-row>

    <div class="country">
      <b-row>
        <h6><strong>Country</strong></h6>
      </b-row>
      <b-row>
        <b-form-select v-model="user.country" :options="countries">
          <template v-slot:first>
            <option :value="null" disabled
              >-- Please select the country you'd like to check --</option
            >
          </template>
        </b-form-select>
      </b-row>
    </div>

    <div class="agegroup">
      <b-row>
        <h6><strong>Age Group</strong></h6>
      </b-row>
      <b-row>
        <b-form-select v-model="user.agegroup" :options="agegroups">
          <template v-slot:first>
            <option :value="null" disabled
              >-- Please select your age group --</option
            >
          </template>
        </b-form-select>
      </b-row>
    </div>

    <div class="alli">
      <b-row>
        <b-col>
          <p
            style="font-size:medium;margin-right:15px;margin-left:15px;text-align:left;"
          >
            Insert your servings per week for each food item of the following
            categories:
          </p>
        </b-col>
      </b-row>

      <b-row>
        <b-col class="little_things">
          <food-items-multiselect
            category="Fruit"
            :value="user.foodItems.fruit"
          ></food-items-multiselect>
        </b-col>
        <b-col class="little_things">
          <food-items-multiselect
            category="Grain"
            :value="user.foodItems.grain"
          ></food-items-multiselect>
        </b-col>
      </b-row>

      <b-row>
        <b-col class="little_things">
          <food-items-multiselect
            category="Vegetable"
            :value="user.foodItems.vegetable"
          ></food-items-multiselect>
        </b-col>
        <b-col class="little_things">
          <food-items-multiselect
            category="Dairy"
            :value="user.foodItems.dairy"
          ></food-items-multiselect>
        </b-col>
      </b-row>

      <b-row>
        <b-col class="little_things">
          <food-items-multiselect
            category="Nut_Seed_Legume"
            :value="user.foodItems.nut_seed_legume"
          ></food-items-multiselect>
        </b-col>
        <b-col class="little_things">
          <food-items-multiselect
            category="Meat"
            :value="user.foodItems.meat"
          ></food-items-multiselect>
        </b-col>
      </b-row>

      <b-row>
        <b-col class="little_things">
          <food-items-multiselect
            category="Oil"
            :value="user.foodItems.oil"
          ></food-items-multiselect>
        </b-col>
        <b-col class="little_things">
          <food-items-multiselect
            category="Other"
            :value="user.foodItems.other"
          ></food-items-multiselect>
        </b-col>
      </b-row>
    </div>
  </b-container>
</template>

<script>
import FoodItemsMultiselect from "@/components/FoodItemsMultiselect";

export default {
  name: "UserInputForm",
  components: { FoodItemsMultiselect },
  props: ["user"],
  data() {
    return {
      countries: [],
      agegroups: []
    };
  },
  mounted() {
    this.$http.get("/country/all").then(response => {
      this.countries = response.data;
    });
    this.$http.get("/agegroup/all").then(response => {
      this.agegroups = response.data;
    });
  }
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style>
.country,
.agegroup {
  padding-top: 10px;
  padding-bottom: 10px;
  padding-right: 20px;
  padding-left: 20px;
}
.little_things {
  padding-top: 10px;
  padding-bottom: 10px;
  padding-right: 32px !important;
  padding-left: 32px !important;
}
.alli {
  padding-top: 40px;
  padding-bottom: 40px;
}
</style>
