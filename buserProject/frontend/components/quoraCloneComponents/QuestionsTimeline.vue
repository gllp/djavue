<template>
   <v-list three-line>
   <template v-for="(question_wrapper, index) in sortQuestions">
        <v-list-tile :key="question_wrapper.question.title">
          <v-list-tile-avatar>
            <img src="https://img.icons8.com/bubbles/2x/question-mark.png">
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>
            <router-link :to="{name: 'quoraclone-user-username-questiontitle', params: {username: question_wrapper.question.author_username, questiontitle: question_wrapper.question.title}}">{{question_wrapper.question.title}}</router-link> - {{question_wrapper.question.created_at | timelapsed}}</v-list-tile-title>
            <v-list-tile-sub-title>
              <v-layout align-center row>
                <v-avatar
                  slot="activator"
                  size="24px">
                  <img :src="question_wrapper.details.avatar">
                </v-avatar>
                <router-link :to="{name: 'quoraclone-user-username', params: {username: question_wrapper.question.author_username}}">{{question_wrapper.question.author_name}}</router-link> 
                 - {{question_wrapper.details.description}}
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
  computed: {
    sortQuestions() {
      return this.questions.concat().sort((question1, question2) => new Date(question2.question.created_at) - new Date(question1.question.created_at))
    }
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
