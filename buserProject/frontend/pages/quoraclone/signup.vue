<template>
    <v-form>
      <v-text-field
        v-model="user.first_name" label="FirstName" required
      ></v-text-field>
      <v-text-field
        v-model="user.last_name" label="LastName"
      ></v-text-field>
      <v-text-field
        v-model="user.username" label="Username" required
      ></v-text-field>
      <v-text-field
        v-model="user.email" label="E-mail" required
      ></v-text-field>
      <v-text-field
        v-model="user.password" type="password" label="Password" required
      ></v-text-field>
      <v-text-field
        v-model="user.description" label="Description"
      ></v-text-field>
      <v-btn :loading="signing" @click="sign">Sign</v-btn>
    </v-form>
</template>

<script>

import AppApi from '~apijs'

export default {
  layout: "quoraclone",
  data () {
    return {
      user: {
        first_name: '',
        last_name: '',
        username: '',
        email: '',
        password: '',
        description: '',
      },
      signing: false,
    }
  },
  methods: {
    sign() {
      this.signing = true
      AppApi.post_new_user(this.user).then(response => {
        this.signing = false
        this.$router.push({name: 'quoraclone'})
      })
    }
  }
}
</script>

<style>
</style>