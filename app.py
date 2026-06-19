import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="GPA 2 Kỳ Calculator",
    page_icon="📚",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("📚 GPA 2 Kỳ Calculator")
st.markdown(
    "Kiểm tra xem GPA chung có thể được tạo từ hai kỳ học với xếp loại đã chọn hay không."
)

# =========================
# KHOẢNG GPA
# =========================
grades = {
    "Khá": (2.5, 3.2),
    "Giỏi": (3.2, 3.6),
    "Xuất sắc": (3.6, 4.0)
}

# =========================
# INPUT
# =========================
z = st.number_input(
    "Nhập GPA chung (Z)",
    min_value=0.00,
    max_value=4.00,
    step=0.01,
    format="%.2f"
)

x_type = st.selectbox(
    "Xếp loại kỳ X",
    list(grades.keys())
)

y_type = st.selectbox(
    "Xếp loại kỳ Y",
    list(grades.keys())
)

# =========================
# XỬ LÝ
# =========================
if st.button("🔍 Kiểm tra"):

    a, b = grades[x_type]
    c, d = grades[y_type]

    # Khoảng GPA chung có thể đạt
    z_min = (a + c) / 2
    z_max = (b + d) / 2

    st.subheader("📊 Kết quả")

    st.write(
        f"GPA chung có thể đạt với tổ hợp này nằm trong khoảng: "
        f"**[{z_min:.2f} ; {z_max:.2f})**"
    )

    if z_min <= z < z_max:

        st.success("✅ Có thể tồn tại GPA của hai kỳ thỏa mãn điều kiện.")

        total = 2 * z

        # Khoảng GPA có thể của kỳ X
        x_min = max(a, total - d)
        x_max = min(b, total - c)

        # Khoảng GPA có thể của kỳ Y
        y_min = total - x_max
        y_max = total - x_min

        st.markdown("---")

        st.write("### GPA có thể của kỳ X")
        st.info(f"{x_min:.2f} → {x_max:.2f}")

        st.write("### GPA có thể của kỳ Y")
        st.info(f"{y_min:.2f} → {y_max:.2f}")

        st.markdown("---")

        st.write(f"📌 Công thức sử dụng:")
        st.latex(r"X + Y = 2Z")

    else:
        st.error("❌ Không tồn tại GPA của hai kỳ thỏa mãn điều kiện này.")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("GPA 2 Kỳ Calculator")
