<template>
  <b-container id="user-footprint-gauge" class="user-footprint-gauge">
    <b-row>
      <b-col>
        <h5><strong>My Carbon Food Print</strong></h5>
      </b-col>
      <b-col>
        <h5><strong>My Country Carbon Food Print</strong></h5>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-card>
          <VueSvgGauge
            class="mini-gauge"
            :start-angle="-110"
            :end-angle="110"
            :value="userCarbonFootprint"
            :separator-step="10"
            :min="0"
            :max="100"
            :gauge-color="[
              { offset: 0, color: '#007bff' },
              { offset: 100, color: '#8CDFAD' }
            ]"
            :transition-duration="2500"
            :scale-interval="5"
          >
            <div class="inner-text">
              <span>{{ userCarbonFootprint }} kgCO2e</span>
            </div>
          </VueSvgGauge>
        </b-card>
      </b-col>
      <b-col>
        <b-card>
          <VueSvgGauge
            class="mini-gauge"
            :start-angle="-110"
            :end-angle="110"
            :value="countryCarbonFootprint"
            :separator-step="10"
            :min="0"
            :max="100"
            :gauge-color="[
              { offset: 0, color: '#007bff' },
              { offset: 100, color: '#8CDFAD' }
            ]"
            :transition-duration="2500"
            :scale-interval="5"
          >
            <div class="inner-text">
              <span>{{ countryCarbonFootprint }} kgCO2e</span>
            </div>
          </VueSvgGauge>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "UserFootprintGauge",
  props: ["userCarbonFootprint", "countryCarbonFootprint"]
};
</script>

<style>
.user-footprint-gauge {
  padding-bottom: 50px;
}

.user-footprint-gauge .inner-text {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  margin-top: 20px;
  padding-top: 20px;
  padding-bottom: 60px !important;
}

.user-footprint-gauge span {
  max-width: 100px;
  margin-top: 70px;
}
</style>
