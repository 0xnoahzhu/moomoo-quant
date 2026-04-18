from moomoo import RET_OK, OpenQuoteContext, SysConfig, UserSecurityGroupType

SysConfig.enable_proto_encrypt(is_encrypt=True)
SysConfig.set_init_rsa_file("/Users/noah/Downloads/conn_key.pem")

quote_ctx = OpenQuoteContext(host="10.1.2.41", port=11111)  # 创建行情对象


ret, groups = quote_ctx.get_user_security_group(group_type=UserSecurityGroupType.ALL)
if ret != RET_OK:
    raise RuntimeError(f"拉分组失败: {groups}")

print("分组列表:")
print(groups)

for group_name in groups["group_name"]:
    ret, stocks = quote_ctx.get_user_security(group_name)
    if ret != RET_OK:
        print(f"[{group_name}] 拉取失败: {stocks}")
        continue
    codes = stocks["code"].tolist() if not stocks.empty else []
    print(f"\n[{group_name}] {len(codes)} 只: {codes}")
quote_ctx.close()
