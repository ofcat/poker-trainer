<script> 
    async function fetchData() { 
        const response = await fetch('http://127.0.0.1:8000/api/hello'); 
        const data = await response.json(); 
        return data.message; } 
</script>

<main>

	</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>