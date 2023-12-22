const request_url = require("supertest")("http://barru.pythonanywhere.com"); // URL NGARAH KESINI
const validasi = require("chai").expect;

describe("Verify Login Feature", function () { // TEST SCENARIO
  it("Verify succes login with data valid", async function () { // TEST CASE
    const response = await request_url // INI NGARAH KE URL BARRU.PYTHONANYWHERE.COM
      .post("/login") 
      .set({ apikey: `sadasdkjasdkjashdkajshdkjas` })
      .send({ email: "belajarmocha@gmail.com", password: "belajarmocha" });
  
    
    validasi(response.statusCode).to.eql(200);
    validasi(response.body.status).to.eql('SUCCESS_LOGIN');
    validasi(response.body.message).to.eql('Anda Berhasil Login');
  });

  it("Failed login, with email valid & password not valid", async function () { // TEST CASE
    const response = await request_url // INI NGARAH KE URL BARRU.PYTHONANYWHERE.COM
      .post("/login") 
      .send({ email: "belajarmocha@gmail.com", password: "asdasdasdasd" });

    validasi(response.statusCode).to.eql(420);
    validasi(response.body.status).to.eql('FAILED_LOGIN');
    validasi(response.body.message).to.eql('Email atau Password Anda Salah');
  });
});