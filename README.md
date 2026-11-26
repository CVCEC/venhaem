# Về Nhà Em · Vào Bếp Nhà Em

Trang giới thiệu chương trình **Về Nhà Em** và 8 bài học nấu ăn **Vào Bếp Nhà Em** của **Trường Tiếng Việt Của Em** – Canada Vietnam Cultural & Educational Council (CVCEC): https://venhaem.cvcec.org

## Lưu ý về sử dụng tài liệu · Terms of use

Các hình ảnh, video và tài liệu học trên trang được đăng tải nhằm giới thiệu chương trình và phục vụ việc học, và có thể được dùng cho nghiên cứu về tiếng Việt như một ngoại ngữ. Các nhà nghiên cứu ngôn ngữ muốn tìm hiểu thêm xin liên hệ contact@cvcec.org.

Trang hoàn toàn phi lợi nhuận. Tài liệu không được sử dụng vào mục đích thương mại, và không được sao chép, tải xuống hay chia sẻ lại dưới bất kỳ hình thức nào khi chưa có sự đồng ý bằng văn bản của CVCEC.

The photos, video and learning materials are published to introduce the program and for learning, and may be used for research on Vietnamese as a foreign language (contact: contact@cvcec.org). This site is entirely non-profit. The materials may not be used for any commercial purpose, and may not be copied, downloaded or shared in any form without written permission from CVCEC.

Copyrighted by CVCEC Trường Tiếng Việt Của Em 2026

## Bộ mẫu chung "Làng Trâu Con"

`index.html` và `vao-bep/index.html` nạp bộ mẫu chung từ https://mau.cvcec.org/v1/ (màu góc học `venhaem`). Bộ mẫu tự chèn thanh các góc học (khi mở riêng), dòng bản quyền và liên hệ. Trang nội bộ `giong-ai/` và thư mục `tools/` không gắn bộ mẫu.

## Giọng đọc tiếng Việt (Vào Bếp Nhà Em)

Các câu tiếng Việt dùng giọng AI chuẩn của trường (Google Gemini, giọng Kore, miền Bắc – giống trang vuihoctiengviet), lưu trong `vao-bep/am-ai/`.

**Quy ước (ngoại lệ riêng kho venhaem, xem quy tắc 7 trong `CLAUDE.md`):** trang không gọi `speechSynthesis` trực tiếp, mọi tiếng đọc đi qua bộ mẫu chung.

- Câu **tiếng Việt**: `TTV.phat({ tep: "am-ai/….mp3", chu })`, ưu tiên tệp giọng AI có sẵn. Câu nào chưa có tệp thì bộ mẫu tạm đọc bằng giọng máy và trang ghi cảnh báo trong console. Khi thêm câu mới vào bài, phải tạo tệp giọng cho câu đó (`tools/gan_am.py`). Nút Chậm/Thường đổi tốc độ phát tệp.
- Câu **tiếng Anh**: `TTV.giong.doc(chu, { ngonNgu: "en" })` (giọng máy của thiết bị, vì trường chưa có giọng chuẩn tiếng Anh; máy không có giọng Anh thì im lặng).
- Bộ mẫu chưa nạp (`window.TTV` chưa có): tệp tiếng Việt vẫn phát, tiếng Anh bỏ qua.
- Theo quy tắc 5, trang **không hiện cách đọc (phiên âm)** dưới chữ: người học bấm để nghe tệp giọng chuẩn và đọc chữ tiếng Việt có dấu đầy đủ.

- Danh sách câu: `giong-ai/can-doc.tsv` · trạng thái: `giong-ai/trang-thai.md`
- GitHub Actions (`Giọng đọc AI`) tự chạy mỗi ngày lúc 08:15 UTC cho đến khi đủ; cần secret `GEMINI_API_KEY` trong Settings → Secrets and variables → Actions.

## Ghi kết quả học (Vào Bếp Nhà Em)

Chơi xong một trò của một món, trang gọi `TTV.ghiKetQua` (bộ mẫu chỉ gửi khi trang nằm trong cổng vietclass.cvcec.org và người học đã đăng nhập; ngoài cổng hàm trả `false`):

| Trò | `hoatDong` | `diem` / `diemToiDa` |
|---|---|---|
| 1 · Xếp thứ tự | `order` | số bước đúng chỗ ở lần kiểm tra đầu / số bước |
| 2 · Nghe và chọn | `listen` | số từ chọn đúng / 6 |
| 3 · Nói theo | `speak` | tổng sao các câu / 3 × số câu |

`bai` là mã món (`nem`, `bun-moc`, `pho-ga`, `com-ga`, `pho-cuon`, `bo-la-lot`, `com-chay`, `banh-xeo-chay`), `soTroChoi: 3`, `sao` (0–3) đúng như sao trang hiện, `thoiGianGiay` tính từ lúc mở trò. Sao trên máy vẫn lưu ở khoá `vaobep-stars-v1` như cũ; không có khoá localStorage mới.

### Kết quả từng câu (từ 26-11-2026)

Mỗi lần gọi có thêm `cau: [{ma, tu, dung, mang, loi}]` (tối đa 40) theo hợp đồng của bộ mẫu chung. `tu` luôn là từ/câu **đích** trong dữ liệu món (cắt còn ≤30 ký tự), không bao giờ là lời người học nói; `dung` = đúng ngay lần đầu.

| Trò | `ma` | `mang` | `loi` khi sai |
|---|---|---|---|
| 1 · Xếp thứ tự | `buoc-1`… | `ngu-phap` | `trat-tu` (theo lần kiểm tra đầu) |
| 2 · Nghe và chọn | `tu-1`… (theo `words`) | `nghe-hieu`; máy không có giọng (đọc nghĩa) → `tu-vung` | so từ đích với từ đã chọn bằng `TTV.loaiLoi` (vd. `dau-thanh`), không đoán được → `nghia`; chế độ đọc → `nghia` |
| 3 · Nói theo | `buoc-1`… | `noi` | lần nói đầu: thiếu âm tiết → `am-van`, chỉ sai thanh → `dau-thanh`; tự chấm → `khac` |

Bộ mẫu cũ bỏ qua `cau`; điểm, sao, mã món, mã trò không đổi.
