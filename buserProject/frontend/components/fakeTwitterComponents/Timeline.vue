<template>
   <v-list three-line>
   <template v-for="(tweet, index) in tweets">
   		<v-divider
          v-if="tweet.divider"
          :key="index"
          :inset="tweet.inset"
        ></v-divider>

        <v-list-tile v-else :key="tweet.author_name">
          <v-list-tile-avatar>
            <img :src="tweet.author_avatar">
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title>
            <router-link :to="{name: 'faketwitter-user-username', params: {username: tweet.author_username}}"> {{tweet.author_name}}</router-link> / 
            {{tweet.author_username}} /
            {{tweet.created_at}}</v-list-tile-title>
            <v-list-tile-sub-title>{{tweet.text}}</v-list-tile-sub-title>
          </v-list-tile-content>
        </v-list-tile>
      </template>
    </v-list>
</template>

<script>

export default {
  layout: "faketwitter",
  props: ['tweets'],
  data () {
    return {}
  }
}
</script>

<style>
</style>
