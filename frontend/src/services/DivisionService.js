import { API } from './BaseService'

class DivisionService {
  constructor() {
    this.divisions = []
    this.p4p = {}
  }

  get() {
    return new Promise((resolve, reject) => {
      if (this.divisions.length) {
        return resolve(this.divisions)
      }

      API.get('division/')
        .then(resp => {
          this.divisions = resp.data.result.sort((a, b) => { return b.weight - a.weight })
          this.p4p = this.divisions.pop()
          // this.divisions.reverse()
          return resolve(this.divisions)
        })
        .catch(e => {
          this.errors.push(e)
          return reject(e)
        })
    })
  }
}
export const divisionService = new DivisionService()
