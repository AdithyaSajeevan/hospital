

function initApp() {
  const app = {
    db: null,
    time: null,
    firstTime: localStorage.getItem("first_time") === null,
    activeMenu: 'pos',
    loadingSampleData: false,
    moneys: [2000, 5000, 10000, 20000, 50000, 100000],
    products: [],
    keyword: "",
    cart: [],
    cash: 0,
    change: 0,
    isShowModalReceipt: false,
    receiptNo: null,
    receiptDate: null,
    async initDatabase() {
      this.db = await loadDatabase();
    this.loadProducts();
    },

    filteredProducts() {
      const rg = this.keyword ? new RegExp(this.keyword, "gi") : null;
      return this.products.filter((p) => !rg || p.name.match(rg));
    },
    addToCart(product) {
      const index = this.findCartIndex(product);
      if (index === -1) {
        this.cart.push({
          productId: product.id,
          image: product.image,
          name: product.name,
          price: product.price,
          option: product.option,
          qty: 1,
        });
      } else {
        this.cart[index].qty += 1;
      }
      this.beep();
      this.updateChange();
    },
    findCartIndex(product) {
      return this.cart.findIndex((p) => p.productId === product.id);
    },
    addQty(item, qty) {
      alert('qty')
      item.qty += qty;
      // const index = this.cart.findIndex((i) => i.productId === item.productId);
      if (item.qty < 1) item.qty = 1;
      updateCart();
      // if (index === -1) {
      //   return;
      // }
      // const afterAdd = item.qty + qty;
      // if (afterAdd === 0) {
      //   this.cart.splice(index, 1);
      //   this.clearSound();
      // } else {
      //   this.cart[index].qty = afterAdd;
      //   this.beep();
      // }
      // this.updateChange();
    },
    updateCart() {
        let totalPrice = 0;
        for (let item of cart) {
            totalPrice += item.qty * item.product.price;
        }
        document.querySelector('.text-right').innerText = priceFormat(totalPrice);
    },
    addCash(amount) {      
      this.cash = (this.cash || 0) + amount;
      this.updateChange();
      this.beep();
    },
    getItemsCount() {
      return this.cart.reduce((count, item) => count + item.qty, 0);
    },
    updateChange() {
      this.change = this.cash - this.getTotalPrice();
    },
    updateCash(value) {
      this.cash = parseFloat(value.replace(/[^0-9]+/g, ""));
      this.updateChange();
    },
    getTotalPrice() {
      return this.cart.reduce(
        (total, item) => total + item.qty * item.price,
        0
      );
    },
    submitable() {
      return this.change >= 0 && this.cart.length > 0;
    },
    submit() {
      if (cart.length > 0) {
        alert('submitted')
      }
      // const time = new Date();
      // this.isShowModalReceipt = true;
      // this.receiptNo = `TWPOS-KS-${Math.round(time.getTime() / 1000)}`;
      // this.receiptDate = this.dateFormat(time);
    },
    closeModalReceipt() {
      this.isShowModalReceipt = false;
    },
    dateFormat(date) {
      const formatter = new Intl.DateTimeFormat('id', { dateStyle: 'short', timeStyle: 'short'});
      return formatter.format(date);
    },
    numberFormat(number) {
      return (number || "")
        .toString()
        .replace(/^0|\./g, "")
        .replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1.");
    },
    priceFormat(price) {
      // return number ? `Rp. ${this.numberFormat(number)}` : `Rp. 0`;
      return `$${price.toFixed(2)}`;
    },
      clear() {
      this.cash = 0;
      this.cart = [];
      this.receiptNo = null;
      this.receiptDate = null;
      this.updateChange();
      this.clearSound();
      },
    beep() {
    this.playSound("sound/beep-29.mp3");
    },
    clearSound() {
    this.playSound("sound/button-21.mp3");
    },
    playSound(src) {
    const sound = new Audio();
    sound.src = src;
    sound.play();
    sound.onended = () => delete(sound);
    },
    printAndProceed() {
      const receiptContent = document.getElementById('receipt-content');
      const titleBefore = document.title;
      const printArea = document.getElementById('print-area');

      printArea.innerHTML = receiptContent.innerHTML;
      document.title = this.receiptNo;

      window.print();
      this.isShowModalReceipt = false;

      printArea.innerHTML = '';
      document.title = titleBefore;

      // TODO save sale data to database

      this.clear();
    }
  };

  return app;
}
