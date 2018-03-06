<template>
  <div class="md-layout md-alignment-top-center">
    <md-list>
      <md-list-item>
        <md-icon>move_to_inbox</md-icon>
        <span class="md-list-item-text">Inbox</span>
      </md-list-item>

      <md-list-item>
        <md-icon>send</md-icon>
        <span class="md-list-item-text">Sent Mail</span>
      </md-list-item>

      <md-list-item>
        <md-icon>delete</md-icon>
        <span class="md-list-item-text">Trash</span>
      </md-list-item>

      <md-list-item>
        <md-icon>error</md-icon>
        <span class="md-list-item-text">Spam</span>
      </md-list-item>

      <md-divider class="md-inset"></md-divider>

      <md-list-item>
        <md-avatar>
          <img src="https://placeimg.com/40/40/people/5" alt="People">
        </md-avatar>

        <span class="md-list-item-text">Abbey Christansen</span>

        <md-button class="md-icon-button md-list-action">
          <md-icon class="md-primary">chat_bubble</md-icon>
        </md-button>
      </md-list-item>

      <md-list-item>
        <md-avatar>
          <img src="https://placeimg.com/40/40/people/1" alt="People">
        </md-avatar>

        <span class="md-list-item-text">Alex Nelson</span>

        <md-button class="md-icon-button md-list-action">
          <md-icon class="md-primary">chat_bubble</md-icon>
        </md-button>
      </md-list-item>

      <md-list-item>
        <md-avatar>
          <img src="https://placeimg.com/40/40/people/6" alt="People">
        </md-avatar>

        <span class="md-list-item-text">Mary Johnson</span>

        <md-button class="md-icon-button md-list-action">
          <md-icon>chat_bubble</md-icon>
        </md-button>
      </md-list-item>
    </md-list>
    <router-link :to="{ name: 'DivisionList'}">All divisions</router-link>
  </div>
</template>

<script>
export default {
  name: 'DivisionList',
  data () {
    return {
      title: 'A list of all divisions'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
