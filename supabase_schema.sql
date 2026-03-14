-- ============================================================
-- Yetimall Monitor — Supabase schema (v2)
-- Run this once in your Supabase project's SQL Editor
-- Dashboard → SQL Editor → New query → paste → Run
-- ============================================================

-- ── Step 1：補齊 transactions 欄位（已有的欄位會自動跳過）──────
ALTER TABLE transactions ADD COLUMN IF NOT EXISTS order_id     TEXT;
ALTER TABLE transactions ADD COLUMN IF NOT EXISTS user_id      TEXT;
ALTER TABLE transactions ADD COLUMN IF NOT EXISTS country      TEXT;
ALTER TABLE transactions ADD COLUMN IF NOT EXISTS metadata     TEXT;
ALTER TABLE transactions ADD COLUMN IF NOT EXISTS is_automated INTEGER NOT NULL DEFAULT 0;

-- ── Step 2：設定 order_id 唯一性（去重 UPSERT 需要）───────────
-- 若已有重複資料，此步驟可能報錯，可先清空再執行：
-- DELETE FROM transactions;
ALTER TABLE transactions ADD CONSTRAINT transactions_order_id_key UNIQUE (order_id);

-- ── Step 3：加速查詢索引 ──────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_txn_user_id   ON transactions(user_id);
CREATE INDEX IF NOT EXISTS idx_txn_country   ON transactions(country);
CREATE INDEX IF NOT EXISTS idx_txn_timestamp ON transactions(timestamp);

-- ════════════════════════════════════════════════════════════
-- 若 transactions 表根本不存在，改跑這個（全新建立）
-- ════════════════════════════════════════════════════════════
-- CREATE TABLE IF NOT EXISTS transactions (
--     id           BIGSERIAL PRIMARY KEY,
--     order_id     TEXT UNIQUE,
--     user_id      TEXT,
--     quantity     INTEGER NOT NULL DEFAULT 1,
--     timestamp    TEXT    NOT NULL,
--     country      TEXT,
--     metadata     TEXT,
--     is_automated INTEGER NOT NULL DEFAULT 0
-- );
