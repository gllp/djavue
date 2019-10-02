<template>
   <v-list three-line>
   <template v-for="(question, index) in questions">
        <v-list-tile :key="question.question_title">
          <v-list-tile-avatar>
            <img src="https://img.icons8.com/bubbles/2x/question-mark.png">
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>
            <router-link :to="{name: 'quoraclone-questionid', params: {questionid: question.id}}">{{question.title}}</router-link> - {{question.created_at | timelapsed}}</v-list-tile-title>
            <v-list-tile-sub-title>
              <v-layout align-center row>
                <v-avatar
                  slot="activator"
                  size="24px">
                  <img :src="question.author_avatar">
                </v-avatar>
                <router-link :to="{name: 'quoraclone-user-username', params: {username: question.author_username}}">{{question.author_name}}</router-link> 
                 - {{question.author_description}}
              </v-layout>
            </v-list-tile-sub-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-divider
          v-if="index + 1 < questions.length" :key="index"
        ></v-divider>
      </template>
    </v-list>
</template>

<script>

export default {
  layout: "quoraclone",
  props: ['questions'],
  data () {
    return {}
  }
}
</script>

<style>
</style>
