import axios from 'axios'

export const API = axios.create({
  baseURL: 'api/v1/',
  headers: {
    'Content-Type': 'application/json'
  }
})
