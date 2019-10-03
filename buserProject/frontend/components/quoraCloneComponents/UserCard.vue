<template>
  <v-card color="cyan darken-2" class="white--text">
    <v-container fluid grid-list-lg>
      <v-layout row>
        <v-flex xs7>
          <div>
            <div class="headline">{{user.username}}</div>
            <div>{{user.description}}</div>
          </div>
        </v-flex>
        <v-flex xs5>
          <v-avatar
            slot="activator"
            size="125px">
            <img :src="user.avatar">
          </v-avatar>
          <div v-if="logged_user && logged_user.username != user.username">
            <v-btn v-if="!user.ifollow" :loading="loading" color="success" @click="follow">Follow</v-btn>
            <v-btn v-if="user.ifollow" :loading="loading" color="error" @click="unfollow">UnFollow</v-btn>
          </div>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card>
</template>

<script>

import AppApi from '~apijs'
import Snacks from '~/helpers/Snacks.js'

export default {
  props: ['user'],
  layout: "quoraclone",
  computed: {
    logged_user() {
      return this.$store.getters.logged_user
    }
  },
  methods: {
    follow() {
      this.loading = true
      AppApi.follow(this.user.username).then(() => {
        this.user.ifollow = true
        this.loading = false
        Snacks.show(this.$store, {
          text: 'You\'re now following ' + this.user.username,
          timeout: 3000})
      })
    },
    unfollow() {
      this.loading = true
      AppApi.unfollow(this.user.username).then(() => {
        this.user.ifollow = false
        this.loading = false
        Snacks.show(this.$store, {
          text: 'You\'re not following ' + this.user.username,
          color: 'error',
          timeout: 3000})
      })
    }
  },
  data () {
    return {
      loading: false
    }
  }
}
</script>

<style>
</style>
