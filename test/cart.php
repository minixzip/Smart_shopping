<?php
$hostname = "172.30.1.32:3306";
$username = "root";
$password = "0000";

// MySQL 연결
$conn = new mysqli($hostname, $username, $password, "products");
$conn->set_charset("utf8"); // 한글 깨짐 방지

// 각 item_num에 대한 상품 데이터를 가져오는 함수
function getProduct($conn, $item_num) {
    $sql = "SELECT * FROM item WHERE NUMBER='$item_num'";
    $result = mysqli_query($conn, $sql);
    $res_row = array();
    if ($result) {
        while ($row = mysqli_fetch_array($result)) {
            array_push($res_row, array(
                'number' => $row[0],    // 번호
                'engname' => $row[1],   // 영어 이름
                'korname' => $row[2],   // 한글 이름
                'info' => $row[3],      // 정보
                'image' => $row[4],     // 이미지
                'price' => $row[5],     // 가격
                'count' => $row[6]  // 마지막 열 (7번째 열)
            ));
        }
    }
    return $res_row;
}

// item_num에 따라 해당하는 행의 마지막 열을 세 번째 열의 값만큼 증가시키는 함수
function incrementLastColumn($conn, $item_num, $incrementValue) {
    // item_num에 해당하는 행의 마지막 열을 incrementValue만큼 증가시키는 쿼리
    $updateSql = "UPDATE item SET count = count + $incrementValue WHERE NUMBER = $item_num";
    mysqli_query($conn, $updateSql);
}

// CSV 파일에서 첫 번째 열의 값이 5인 행을 찾아 2번째, 3번째 열 값을 불러오고, item_num 값을 조건에 따라 설정하는 함수
function getSpecificRows($file) {
    $specificData = array(); // 결과를 저장할 배열
    $existingItemNums = array(); // 중복 체크를 위한 배열

    // CSV 파일을 열기
    if (($handle = fopen($file, "r")) !== FALSE) {
        // CSV 파일의 각 행을 반복
        while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            // 첫 번째 열의 값이 5인지 확인
            if ($data[0] == '5') {
                $item_num = null; // item_num 초기화
                // 2번째 열의 값에 따라 item_num 설정
                if ($data[1] == 'ramen') {
                    $item_num = 3; // ramen일 경우 3
                } elseif ($data[1] == 'cocacola') {
                    $item_num = 2; // cocacola일 경우 2
                } elseif ($data[1] == 'cancho') {
                    $item_num = 1; // cancho일 경우 1
                }

                // item_num이 설정된 경우, 데이터를 배열에 추가
                if ($item_num !== null && !in_array($item_num, $existingItemNums)) {
                    $specificData[] = array(
                        'item_num' => $item_num,   // 설정된 item_num
                        'column2' => $data[1],     // 두 번째 열
                        'column3' => $data[2]      // 세 번째 열
                    );
                    $existingItemNums[] = $item_num; // 중복 체크를 위해 추가
                }
            }
        }
        fclose($handle); // 파일을 다 읽었으면 닫기
    }

    return $specificData; // 결과 반환
}

// CSV 파일을 처리하는 함수
function processCSV($file, $conn) {
    $csvData = array();
    if (($handle = fopen($file, "r")) !== FALSE) { // 파일을 열고 읽기 모드로 핸들러 생성
        while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) { // 한 줄씩 CSV 파일을 읽음
            // 첫 번째 열의 값이 5인지 확인
            if ($data[0] == '5') {
                // item_num 값을 조건에 따라 설정
                $item_num = null;
                if ($data[1] == 'ramen') {
                    $item_num = 3; // ramen일 경우 3
                } elseif ($data[1] == 'cocacola') {
                    $item_num = 2; // cocacola일 경우 2
                } elseif ($data[1] == 'cancho') {
                    $item_num = 1; // cancho일 경우 1
                }

                // item_num이 설정된 경우, DB에서 상품 정보 불러오기
                if ($item_num !== null) {
                    $product = getProduct($conn, $item_num);
                    
                    // 세 번째 열의 값만큼 마지막 열을 증가
                    $incrementValue = (int)$data[2]; // 세 번째 열의 값을 정수로 변환
                    incrementLastColumn($conn, $item_num, $incrementValue);
                    
                    // 불러온 상품 정보를 배열에 추가
                    if (!empty($product)) {
                        array_push($csvData, $product[0]); // getProduct는 배열을 반환하므로 [0]으로 접근
                    }
                }
            }
        }
        fclose($handle); // 파일 닫기
    }
    return $csvData;
}

// 서버 내 경로에 있는 CSV 파일을 불러오는 코드
$csvFilePath = "/home/khung/yolov5/runs/detect/exp"; // 경로 설정 (절대 경로 사용)
$csvFileName = "cart_items.csv"; // 파일 이름 설정
$csvFileFullPath = $csvFilePath . '/' . $csvFileName; // 파일 전체 경로 생성

// echo $csvFileFullPath;
$csvData = array();
if (file_exists($csvFileFullPath)) { // 경로에 파일이 존재하는지 확인
    $csvData = processCSV($csvFileFullPath, $conn); // 파일이 존재하면 처리
} else {
    echo "Dosen't find file CSV.";
}

// 첫 번째 열의 값이 5인 행에서 2번째와 3번째 열을 불러오기
$specificRows = getSpecificRows($csvFileFullPath);

$conn->close();
?>

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cart</title>
    <style>
        /* 스타일 동일, 생략 */
    </style>
</head>
<body>
    <header>
        <h1>Cart</h1>
    </header>
    <main>
        <div class="cart-container">
            <div id="cart-items"></div>

            <div class="cart-total">
                Total: <span id="cart-total">0</span> \
            </div>
            <button class="checkout-btn" onclick="checkout()">Order</button>

            <!-- CSV 파일이 서버 경로에서 자동으로 로드되므로, 업로드 폼을 제거 -->
        </div>
    </main>

    <script>
        let cart = [];
        
        // 서버 경로에서 불러온 CSV 파일에서 가져온 상품 데이터를 자바스크립트로 전달
        const csvProducts = <?php echo isset($csvData) ? json_encode($csvData) : '[]'; ?>;

        // 장바구니에 상품을 추가하는 함수
        function addToCart(product) {
            const existingItem = cart.find(item => item.number === product.number);

            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                product.quantity = 1;
                cart.push(product);
            }

            renderCart();
        }

        // 상품의 수량을 변경하는 함수
        function changeQuantity(productNumber, amount) {
            const item = cart.find(item => item.number === productNumber);

            if (item) {
                item.quantity += amount;
                if (item.quantity <= 0) {
                    cart = cart.filter(item => item.number !== productNumber);
                }
            }

            renderCart();
        }

        // 장바구니 렌더링
        function renderCart() {
            const cartItemsContainer = document.getElementById('cart-items');
            cartItemsContainer.innerHTML = '';

            let total = 0;

            cart.forEach(item => {
                const itemTotal = item.price * item.quantity;
                total += itemTotal;

                const cartItem = document.createElement('div');
                cartItem.className = 'cart-item';

                cartItem.innerHTML = `
                    <img src="${item.image}" alt="${item.engname}">
                    <div class="cart-item-info">
                        <div class="cart-item-name">${item.korname}</div>
                        <div class="quantity-controls">
                            <button onclick="changeQuantity(${item.number}, -1)">-</button>
                            <span>${item.quantity}</span>
                            <button onclick="changeQuantity(${item.number}, 1)">+</button>
                        </div>
                    </div>
                    <div class="cart-item-price">${itemTotal} \</div>
                `;

                cartItemsContainer.appendChild(cartItem);
            });

            document.getElementById('cart-total').textContent = total;
        }

        // 결제하기 버튼
        function checkout() {
            alert(`Merchandise Total is ${document.getElementById('cart-total').textContent} \.`);
        }

        // 서버 경로에서 불러온 상품을 장바구니에 추가
        csvProducts.forEach(product => {
            addToCart(product);
        });

    </script>
</body>
</html>
