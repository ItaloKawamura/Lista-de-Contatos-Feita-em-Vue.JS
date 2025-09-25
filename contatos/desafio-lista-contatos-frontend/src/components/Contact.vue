<script>
export default {
    name: 'Contact',
    props: {
        contact: {
            type: Object,
            required: true
        }
    }
}
</script>

<template>
    <div>
         <img :src="contact.foto" :alt="'Foto de ' + contact.nome"/>
         <p>{{ contact.nome }}</p>
         <p>{{ contact.email }}</p>
    </div>
</template>

<style scoped>
img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 10px;
}

p {
    display: inline-block;
    margin: 0;
    padding-right: 10px;
}

div {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}
</style>