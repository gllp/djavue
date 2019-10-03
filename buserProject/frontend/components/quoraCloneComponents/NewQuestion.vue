<template>
<div>
  <v-btn color="blue" block v-if="logged_user" @click="goquestion()">New Question</v-btn>
  <textarea-dialog ref="newquestiondialog"></textarea-dialog>
</div>
</template>

<script>

import textareaDialog from '~/components/TextAreaDialog.vue'
import AppApi from '~apijs'

export default {
  layout: "quoraclone",
  components: {
    textareaDialog
  },
  computed: {
    logged_user() {
      return this.$store.getters.logged_user
    }
  },
  data () {
    return {}
  },
  methods: {
    goquestion () {
      this.$refs.newquestiondialog.open({
        title: "New Question",
        label: "Type the new question",
        value: '',
        action: 'Post Question',
        actionFunc: value => {
          return AppApi.post_question(value).then(question => {
            this.$emit('newquestion', question)});
        }
      })
    }
  }
}
</script>

<style>
</style>