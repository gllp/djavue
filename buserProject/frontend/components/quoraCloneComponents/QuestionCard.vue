<template>
	<v-card color="blue lighten-3">
    <v-container fluid grid-list-lg>
      <v-layout row>
        <v-flex xs7>
          <div>
            <div class="headline">
             <strong>{{questionwrapper.question.title}}
             </strong>
            </div>
            <div style="padding-top: 8px;">
              <v-avatar
                slot="activator"
                size="80px"
                >
              <img
                :src="questionwrapper.details.avatar">
            </v-avatar> 
              <v-layout row v-if="questionwrapper.details.description.length > 0"> 
                  <router-link :to="{name: 'quoraclone-user-username', params: {username: questionwrapper.question.author_username}}"> {{questionwrapper.question.author_name}}
                </router-link> 
                - {{questionwrapper.details.description}}
            </v-layout>
            <v-layout row v-else> 
              <router-link :to="{name: 'quoraclone-user-username', params: {username: questionwrapper.question.author_username}}"> {{questionwrapper.question.author_name}}
                </router-link> 
            </v-layout>
            </div>
          </div>
        </v-flex>
        <v-flex xs5>
          <v-card-media
            src="https://img.icons8.com/bubbles/2x/question-mark.png"
            height="125px"
            contain
          ></v-card-media>
        </v-flex>
      </v-layout>
    </v-container>
    <v-card color="blue lighten-4">
      <v-card-title primary-title>
          <div>
            <h3 class="headline mb-0">Answers</h3>
          </div>
        </v-card-title>
      <v-list two-line v-if="answers.length > 0">
         <v-list-group 
              v-for="answerwrapper in answers"
              :key="answerwrapper.answer.text"
              no-action
            >
            <v-list-tile slot="activator">
              <v-list-tile-content>
                <v-list-tile-title><v-avatar
                  slot="activator"
                  size="22px"
                  >
                <img
                  :src="answerwrapper.details.avatar">
              </v-avatar> <router-link :to="{name: 'quoraclone-user-username', params: {username: answerwrapper.answer.author_username}}"> {{answerwrapper.answer.author_name}} </router-link> - {{answerwrapper.details.description}}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-layout>
                <v-card color="blue lighten-4">
                  <v-card-text>
                      {{answerwrapper.answer.text}}
                  </v-card-text>
                </v-card>
              </v-layout>
          </v-list-group>
      </v-list>
      <v-card-text v-else>No answers provided for this question</v-card-text>
    </v-card>
  </v-card>
</template>

<script>

export default {
  layout: "quoraclone",
  props: ['questionwrapper', 'answers'],
  data () {
    return {}
  }
}
</script>

<style>
</style>
