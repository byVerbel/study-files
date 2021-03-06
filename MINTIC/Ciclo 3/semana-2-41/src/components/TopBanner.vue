<template>
  <div>
      <top-menu></top-menu>
    <div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
                <li data-target="#carouselExampleCaptions" data-slide-to="0" class="active"></li>
                <li data-target="#carouselExampleCaptions" data-slide-to="1" class=""></li>
                <li data-target="#carouselExampleCaptions" data-slide-to="2" class=""></li>
            </ol>
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img class="bd-placeholder-img bd-placeholder-img-lg d-block w-100" width="800" height="500" src="https://i.pinimg.com/originals/20/17/ec/2017ec5dc3068ca3436950eb75467529.jpg" alt="Animales">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Película</h5>
                        <p>Te mostramos algunas de nuestras películas favoritas.</p>
                    </div>
                </div>
                <div class="carousel-item">
                    <img class="bd-placeholder-img bd-placeholder-img-lg d-block w-100" width="800" height="500" src="https://static.zerochan.net/North.Italy.full.1831826.jpg" alt="Personas">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Animes</h5>
                        <p>Sin duda alguna, ver este anime te cambiará la vida.</p>
                    </div>
                </div>
                <div class="carousel-item">
                    <img class="bd-placeholder-img bd-placeholder-img-lg d-block w-100" width="800" height="500" src="https://mk0coffinmewcea6j79k.kinstacdn.com/wp-content/uploads/Trainees-2019-800x500.jpg" alt="Naturaleza">
                    <div class="carousel-caption d-none d-md-block">
                        <h5>Equipo</h5>
                        <p>Nos presentamos.</p>
                    </div>
                </div>
            </div>
            <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
        </div>
  </div>
</template>

<script>
import TopMenu from './TopMenu';
 
export default {
  name: "TopBanner",
  components:{
      TopMenu
  }
};
</script>

<style scoped>
</style>