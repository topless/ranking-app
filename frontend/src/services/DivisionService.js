import { HTTP } from './BaseService'

class DivisionService {
  constructor() {
    this.divisions = []
  }

  get() {
    return new Promise((resolve, reject) => {
      if (this.divisions.length) {
        return resolve(this.divisions)
      }

      HTTP.get('division/')
        .then(resp => {
          this.divisions = resp.data.result.sort(function(a, b) {
            return b.weight - a.weight
          })
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
