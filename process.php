<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $phone = htmlspecialchars($_POST['phone']);
    $address = htmlspecialchars($_POST['address']);
    $product = htmlspecialchars($_POST['product']);

    // معالجة الطلب أو تخزينه في قاعدة بيانات
    $message = "تم استلام الطلب بنجاح:\n";
    $message .= "الاسم: $name\n";
    $message .= "رقم الهاتف: $phone\n";
    $message .= "العنوان: $address\n";
    $message .= "المنتج المطلوب: $product\n";

    // إرسال التأكيد إلى الزبون (اختياري)
    // mail($email, "تأكيد الطلب", $message);

    echo "<h1>شكراً لك $name!</h1>";
    echo "<p>تم استلام طلبك بنجاح وسنتواصل معك قريبًا.</p>";
} else {
    echo "يرجى استخدام النموذج لإرسال الطلب.";
}
?>
