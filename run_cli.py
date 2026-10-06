from quality_aggregate.core import Inspection, summarize


if __name__ == "__main__":
    record = Inspection.create("demo", "v1", "draft", "operator", {"场景": "登记生产判读并生成批次摘要"})
    print(summarize(record))
