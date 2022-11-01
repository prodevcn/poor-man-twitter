<script>
import moment from "moment";
import TweetsTable from "./components/TweetsTable.vue";
import TweetPanel from "./components/TweetPanel.vue";

export default {
  name: "App",
  components: {
    TweetsTable,
    TweetPanel,
  },
  data() {
    return {
      tweet: {
        name: "",
        tweet: "",
        datetime: "",
      },
      tweets: [],
    };
  },

  async created() {
    await this.getTweets();
  },

  methods: {
    validator() {
      return (
        this.tweet.name !== undefined &&
        this.tweet.name.length !== 0 &&
        this.tweet.tweet !== undefined &&
        this.tweet.tweet.length !== 0
      );
    },
    async getTweets() {
      let response = await fetch("http://127.0.0.1:8000/api/tweets/");
      this.tweets = await response.json();
    },
    async addTweet() {
      if (!this.validator()) return;
      await this.getTweets();
      await fetch("http://127.0.0.1:8000/api/tweets/", {
        method: "post",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.tweet),
      });
      await this.getTweets();
      this.tweet = {};
    },
    moment,
  },
};
</script>

<template>
  <div class="container">
    <img
      alt="Vue logo"
      class="logo"
      src="./assets/logo.svg"
      width="125"
      height="125"
    />
    <h1 class="title">Poor Man's Twitter</h1>
    <TweetPanel :tweet="tweet" :tweetHandler="this.addTweet" />
    <TweetsTable :tweets="tweets" />
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

.title {
  margin: 2rem 0;
}

.container {
  text-align: center;
  color: #2c3e50;
  margin-top: 2rem;
}
</style>
