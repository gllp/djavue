<template>
  <v-layout justify-center align-center>
    <v-btn color="success" :to="{name: 'todos'}">What TODO next?</v-btn>
    <v-btn color="success" :to="{name: 'faketwitter'}">Go to FakeTwitter</v-btn>
    <v-btn color="success" :to="{name: 'quoraclone'}">Go to QuoraClone</v-btn>
  </v-layout>
</template>

<script>

export default {
  data () {
    return {}
  }
}
</script>

<style>
</style>
