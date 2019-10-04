<template>
  <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-card-media src="userprofile.avatar" height="300px">
        </v-card-media>
        <v-layout class="headline">{{userprofile.first_name}}</v-layout>
        <v-list two-line>
          <v-list-tile>
            <v-list-tile-content>
              <v-list-tile-title>Username: {{userprofile.username}}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-divider inset></v-divider>
          <v-list-tile>
            <v-list-tile-content>
              <v-list-tile-title>Email: {{userprofile.email}}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-divider inset></v-divider>
          <v-list-tile v-if="userprofile.description != ''">
            <v-list-tile-content>
              <v-list-tile-title>User Description: {{userprofile.description}}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>

export default {
  props: ['userprofile'],
  layout: "quoraclone",
  computed: {
    logged_user() {
      return this.$store.getters.logged_user
    }
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
