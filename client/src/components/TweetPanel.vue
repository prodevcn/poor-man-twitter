<script>
import moment from "moment";
export default {
  name: "TweetPanel",
  props: { tweet: Object, tweetHandler: Function },
  methods: {
    moment,
  },
};
</script>
<template>
  <form @submit.prevent="tweetHandler" class="mb-4">
    <div class="form-group row">
      <div class="col">
        <input
          type="text"
          class="form-control col-3 mx-2"
          v-model="tweet.name"
          placeholder="Name"
          minlength="1"
        />
      </div>
      <div class="col">
        <input
          type="text"
          class="form-control col-3 mx-2"
          v-model="tweet.tweet"
          minlength="1"
          placeholder="Tweet"
        />
      </div>
      <div class="col-3 mx-2">
        <button class="btn btn-primary" type="submit">Submit</button>
      </div>
    </div>
  </form>
</template>
