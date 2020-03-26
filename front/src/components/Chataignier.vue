<template>
  <v-container fluid>
    <v-row align="center">
    <v-col cols="6">
      <v-card
        class="mx-auto mt-6"
        max-width="500"
      >
        <v-img
          height="250"
          src="https://www.meillandrichardier.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/1/0/1036-2936-rosier_papa_meilland_meicesar-mi-t1000.jpg"
        ></v-img>

        <v-card-title>Rose 'Papa Meilland'</v-card-title>
        <v-card-subtitle>'Meicesar', 'Meisar'</v-card-subtitle>

        <v-divider class="mx-4"></v-divider>

        <v-card-text>


          <div class="my-4 subtitle-1">
            Rosa 'Papa Meilland' is a cultivar of hybrid tea rose, bred by Meilland International SA in France in 1963.
          </div>

          <div>
            Flowers of dark velvety crimson open from pointed, almost black, buds. <br>
            The blossoms are large and high-centered, with 35 petals, and are borne mostly singly on strong stems. They have a rich scent. Flowering is very sustained over the summer to early autumn. <br>
            The foliage is glossy and bright green. <br>
            It is a vigorous rose, but not as disease-resistant as it once was. <br>
            In the bush form it is 80 to 90 cm (31 to 35 in) high, and it also exists in climbing form (developed by the nursery rosarian Louis Dima in Doué-la-Fontaine, the French capital of roses ).
          </div>
        </v-card-text>
        <v-divider class="mx-4"></v-divider>
        <v-card-actions>
          <v-btn
            color="deep-purple lighten-2"
            text
            href="https://en.wikipedia.org/wiki/Rosa_%27Papa_Meilland%27"
          >
            More information
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
    <v-col>
      <div class="display-1 font-weight-light">
        <p class="text-center">
          Last hour stats&nbsp;
          <v-btn icon color="black">
              <v-icon>mdi-refresh</v-icon>
            </v-btn>
        </p>

      </div>
        <v-divider class="my-5"></v-divider>
        <v-card
          class="mx-auto text-center"
          color="indigo lighten-4"
          dark
          max-width="600"
        >
          <v-card-text>
            <v-sheet color="rgba(0, 0, 0, .12)">
              <v-sparkline
                :value="value_temp"
                color="rgba(255, 255, 255, .7)"
                height="100"
                padding="24"
                stroke-linecap="round"
                label-size="10"
                smooth
              >
                <template v-slot:label="item">
                  {{ item.value }}°C
                </template>
              </v-sparkline>
            </v-sheet>
          </v-card-text>

          <v-card-text>
            <div class="display-1 font-weight-light">Temperature</div>
          </v-card-text>
        </v-card>
      <br>
      <v-card
          class="mx-auto text-center"
          color="deep-purple lighten-4"
          dark
          max-width="600"
        >
          <v-card-text>
            <v-sheet color="rgba(0, 0, 0, .12)">
              <v-sparkline
                :value="value_hum"
                color="rgba(255, 255, 255, .7)"
                height="100"
                padding="24"
                stroke-linecap="round"
                label-size="10"
                smooth
              >
                <template v-slot:label="item">
                  {{ item.value }}%
                </template>
              </v-sparkline>
            </v-sheet>
          </v-card-text>

          <v-card-text>
            <div class="display-1 font-weight-light">Humidity</div>
          </v-card-text>
        </v-card>

    </v-col>
    </v-row>
  </v-container>

</template>


<script>
  const axios = require('axios');

  export default {
    data: () => ({
      value_temp: [],
      value_hum: [],
      time: [],
      loading: false
    }),
    mounted() {
      this.getPlantData();
    },
    methods: {
      getPlantData() {
        this.loading = true;
        axios.get('http://0.0.0.0:5000/api/plantdata').then((response) => {
          this.value_temp = response.data.stats.temperature;
          console.log(this.value_temp);
          this.value_hum = response.data.stats.humidity;
          this.time = response.data.stats.time;
          this.loading = false;
        })
      }
    }
  }
</script>
