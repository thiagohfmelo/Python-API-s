from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

# URL base para o ViaCEP (ou outra API de CEP)
VIA_CEP_URL = "https://viacep.com.br/ws/{cep}/json/"

class Address(BaseModel):
    street: str
    neighborhood: str
    city: str
    state: str
    postal_code: str

@app.get("/address/{cep}", response_model=Address)
async def get_address(cep: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(VIA_CEP_URL.format(cep=cep))
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="CEP not found")
        
        data = response.json()
        
        # Verifica se a resposta contém os dados esperados
        if 'erro' in data:
            raise HTTPException(status_code=404, detail="CEP not found")
        
        address = Address(
            street=data.get('logradouro', ''),
            neighborhood=data.get('bairro', ''),
            city=data.get('localidade', ''),
            state=data.get('uf', ''),
            postal_code=data.get('cep', '')
        )
        
        return address

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
