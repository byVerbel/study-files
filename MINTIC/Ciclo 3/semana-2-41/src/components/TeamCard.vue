<template>
   
        <div class="card text-white bg-info">
            <div class="d-flex justify-content-center p2">
             <img :src="member.image" width="300" height="300" alt="Fotografia Integrantes">
        </div>
        <div class="card-body">
           <h5 class="card-title">{{member.nombre}}</h5>
           <p class="card-text"><span>Código: </span>{{member.codigo}}</p>
           <p class="card-text">{{member.descripcion}}</p>
           <p class="card-text">{{member.rol}}</p>
       </div>
        <div class="card-footer">
        <small class="text-white">Curso Desarrollo Web. Dic. 2020</small>
        </div> 
        </div> 
   
  
</template>

<script>
export default {
  name: "TeamCard",
  props: ['member']
};
</script>

<style scoped>
</style>
