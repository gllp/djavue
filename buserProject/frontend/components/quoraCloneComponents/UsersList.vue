<template>
   <v-list three-line>
   <template v-for="(user, index) in users">
        <v-list-tile :key="user.username">
          <v-list-tile-avatar>
            <img :src="user.avatar">
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>
           {{user.username}}
         </v-list-tile-title>
            <v-list-tile-sub-title>
                {{user.description}}
            </v-list-tile-sub-title>
          </v-list-tile-content>
          <v-list-tile-action>
              <v-btn :to="{name: 'quoraclone-user-username', params: {username: user.username}}">See User Feed</v-btn>
            </v-list-tile-action>
        </v-list-tile>
        <v-divider
          v-if="index + 1 < users.length" :key="index"
        ></v-divider>
      </template>
    </v-list>
</template>

<script>

export default {
  layout: "quoraclone",
  props: ['users'],
  data () {
    return {}
  }
}
</script>

<style>
</style>
