<template>
  <b-container id="food-items-multiselect">
    <b-row>
      <h6 style="font-size:0.8rem;text-align:left">
        <strong>{{ category.replace(/_/g, ' ') }}</strong>
      </h6>
    </b-row>
    <b-row>
      <multiselect
        placeholder="Pick food items"
        label="name"
        :value="value"
        :options="options"
        :multiple="true"
        :searchable="true"
        :allow-empty="true"
        :hide-selected="false"
        :clear-on-select="true"
        :max-height="200"
        @select="onSelect"
        @remove="onRemove"
      ></multiselect>
    </b-row>
    <b-row v-for="food_item in value" :key="food_item.name" class="food-item">
      <b-col cols="4">
        <h6 style="font-size:0.8rem;">{{ food_item.name }}</h6>
      </b-col>
      <b-col>
        <b-form-input
          v-model="food_item.quantity"
          type="range"
          min="0"
          max="20"
        ></b-form-input>
      </b-col>
      <b-col cols="1">
        <h6>{{ food_item.quantity }}</h6>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from 'axios';
import Multiselect from 'vue-multiselect';

export default {
  name: 'FoodItemsMultiselect',
  components: { Multiselect },
  props: ['category', 'value'],
  data() {
    return {
      isDisabled: false,
      isTouched: false,
      options: []
    };
  },
  mounted() {
    axios.get('/food/' + this.category).then(response => {
      this.options = response.data;
    });
  },
  methods: {
    onSelect(option) {
      this.value.push(option);
    },
    onRemove(option) {
      this.value.splice(this.value.indexOf(option), 1);
      this.options[this.options.indexOf(option)].quantity = 0;
    }
  }
};
</script>

<style>
.food-item {
  padding-top: 5px;
}
</style>
