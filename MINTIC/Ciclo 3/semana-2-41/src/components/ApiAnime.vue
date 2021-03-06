<template>
    <div class="row">
      <div class="col-lg-6 col-xs-12 border" v-for="(anime, index) of animes" :key="index">
        <div class="d-flex justify-content-center align-items-center">
          <div class="p-3">
            <img :src="anime.image_url" alt="anime poster">
          </div>
          <div class="p-2">
              <h2>{{anime.title}}</h2>
              <hr>
            <h5>Descripción en inglés...</h5>
            <p>{{anime.synopsis}}</p>
          </div>
          <div class="d-flex container-fluid justify-content-end pb-2 mt-n2">
            <a :href="'https://myanimelist.net//anime//'+anime.mal_id" target="_blank" class="btn btn-outline-info">Leer más</a>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ApiAnime",
  data() {
    return {
      animes: null,
    };
  },
  mounted() {
    axios
      .get("https://api.jikan.moe/v3/search/anime?q=shingeki%20no%20kyojin%20season")
      .then((response) => {
        this.animes = response.data.results.slice(0, 4);
        console.log(this.animes);
      });
  },
};
</script>

<style scoped>
</style>