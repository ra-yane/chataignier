<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
      flat
    >
      <div class="d-flex align-center">
        <v-img
          class="shrink mr-2"
          contain
          src="./assets/logo.png"
          transition="scale-transition"
          width="40"
        />

        <v-toolbar-title class="display-1 font-weight-light">Châtaignier</v-toolbar-title>
      </div>

      <v-spacer></v-spacer>

        <v-btn
          color="primary"
          depressed
          @click="dialog = true"
        >
          Set my alarms
        </v-btn>
      <div class="text-center">
        <v-dialog
          v-model="dialog"
          width="500"
        >
       <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          Alarms Panel
        </v-card-title>

        <v-card-text>
          <v-text-field
          v-model="temperature"
          label="Temperature"
        ></v-text-field>
          <v-text-field
          v-model="humidity"
          label="Humidity"
        ></v-text-field>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
    </v-app-bar>

    <v-content>
      <Chataignier/>
    </v-content>
  </v-app>
</template>

<script>
import Chataignier from './components/Chataignier';

export default {
  name: 'App',

  components: {
    Chataignier,
  },

  data: () => ({
    dialog: false,
    temperature: 26,
    humidity: 53
  }),
};
</script>
